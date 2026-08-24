"""Flask application for my portfolio.
"""

import re
from datetime import datetime

from flask import Flask, render_template, request
from markupsafe import Markup, escape

import content

# Matches a backtick code span or a [text](url) link, whichever comes first.
_RICHTEXT_TOKEN = re.compile(r"`([^`]+)`|\[([^\]]+)\]\(([^)]+)\)")


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

    @app.template_filter("richtext")
    def richtext(text):
        """Render backtick code spans and ``[text](url)`` links as safe HTML.

        Used for prose written with lightweight inline markup, like the writing
        page's paragraphs, where plain ``inline_code`` isn't enough because the
        source also contains links to PRs and commits.

        Args:
            text: Source string, possibly containing backtick spans and/or
                ``[text](url)`` links.

        Returns:
            markupsafe.Markup: Escaped HTML with code spans and links applied.
        """
        source = str(text)
        rendered = []
        cursor = 0
        for match in _RICHTEXT_TOKEN.finditer(source):
            rendered.append(str(escape(source[cursor:match.start()])))
            code_text, link_text, link_url = match.groups()
            if code_text is not None:
                rendered.append(f"<code>{escape(code_text)}</code>")
            else:
                rendered.append(
                    f'<a href="{escape(link_url)}" target="_blank" rel="noopener">'
                    f"{escape(link_text)}</a>"
                )
            cursor = match.end()
        rendered.append(str(escape(source[cursor:])))
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
    """Register the site's page routes.

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

    # Permanent slug: this is the GSoC final-work-product URL, so it must never
    # be renamed once submitted.
    @app.route("/writing/reproducible-builds-konflux-gsoc")
    def writing():
        """Render the GSoC final-report page."""
        return render_template("writing.html", writing=content.get_writing())


# Module-level WSGI callable for gunicorn (Procfile: web: gunicorn app:app)
# and for `flask --app app run`.
app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
