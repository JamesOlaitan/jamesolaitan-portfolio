"""Flask application for my portfolio.
"""

from datetime import datetime

from flask import Flask, render_template, request
from markupsafe import Markup, escape

import content


def create_app():
    """Build and configure the Flask application.

    Uses the application-factory pattern for testability and clean configuration,
    while still exposing a module-level ``app`` (below) for the WSGI server.

    Returns:
        Flask: A configured application instance with routes and template context
        registered.
    """
    app = Flask(__name__)
    _register_template_context(app)
    _register_template_filters(app)
    _register_routes(app)
    return app


def _register_template_filters(app):
    """Register Jinja filters used by the templates.

    Args:
        app: The Flask application to attach filters to.
    """

    @app.template_filter("inline_code")
    def inline_code(text):
        """Render backtick-delimited spans as ``<code>`` elements.

        Splits on backticks and wraps the odd segments (the quoted terms) in
        ``<code>``. All text is HTML-escaped first, so the result is safe to mark
        up. Used for inline terms like ``grep`` / ``ps`` / ``journald``.

        Args:
            text: Source string, possibly containing ```term``` spans.

        Returns:
            markupsafe.Markup: Escaped HTML with code spans applied.
        """
        segments = str(text).split("`")
        rendered = []
        for index, segment in enumerate(segments):
            escaped = str(escape(segment))
            rendered.append(f"<code>{escaped}</code>" if index % 2 else escaped)
        return Markup("".join(rendered))


def _register_template_context(app):
    """Inject values every template needs (chrome, footer, social tags).

    Args:
        app: The Flask application to attach the context processor to.
    """

    @app.context_processor
    def inject_globals():
        """Provide ``profile``, ``current_year``, and ``canonical_url`` to all templates."""
        return {
            "profile": content.get_profile(),
            "current_year": datetime.now().year,
            # Absolute URL of the current page, used for Open Graph / canonical tags.
            "canonical_url": request.base_url,
        }


def _register_routes(app):
    """Register the site's three page routes.

    Args:
        app: The Flask application to attach routes to.
    """

    @app.route("/")
    def index():
        """Render the home page: hero, selected work, experience, and contact."""
        return render_template(
            "index.html",
            projects=content.get_projects(),
            experience=content.get_experience(),
        )

    @app.route("/about")
    def about():
        """Render the About page."""
        return render_template("about.html", about=content.get_about())

    @app.route("/reading")
    def reading():
        """Render the Reading page."""
        return render_template("reading.html", reading=content.get_reading())


# Module-level WSGI callable for gunicorn (Procfile: web: gunicorn app:app)
# and for `flask --app app run`.
app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
