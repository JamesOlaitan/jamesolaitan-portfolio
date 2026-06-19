"""Content access layer.

This package is the only place that reads :mod:`content.data`. Routes and templates
depend on these accessor functions rather than the raw module globals, so the storage
of content (Python dicts today; JSON, a CMS, or a database tomorrow) can change without
touching the rest of the app.

Returned values reference the underlying module globals for efficiency. Content is
read-only at runtime — callers must not mutate the returned objects.
"""

from content import data


def get_profile():
    """Return the site owner's profile.

    Returns:
        dict: Profile fields — ``name``, ``role``, ``hero_clause``, ``supporting``,
        ``location``, ``availability``, ``email``, ``github``, ``linkedin``, ``resume``.
    """
    return data.PROFILE


def get_projects():
    """Return the selected-work projects, in display order.

    Returns:
        list[dict]: Each project has ``name``, ``blurb``, ``year``, ``type``,
        ``domain``, ``lang``, ``repo``, and ``image``.
    """
    return data.PROJECTS


def get_experience():
    """Return the experience entries, in display order.

    Returns:
        list[dict]: Each entry has ``company``, ``logo``, ``role``, ``dates``,
        ``in_progress``, ``impact``, ``tags``, and ``artifact`` (``dict`` or ``None``).
    """
    return data.EXPERIENCE


def get_about():
    """Return the About page content as a single bundle.

    Returns:
        dict: ``paragraphs`` (list[str]) and ``footer`` (str), so the About route and
        template work with one cohesive object instead of two loose globals.
    """
    return {"paragraphs": data.ABOUT_PARAGRAPHS, "footer": data.ABOUT_FOOTER}


def get_reading():
    """Return the reading list, grouped by category.

    Returns:
        list[dict]: Each group has a ``category`` label and an ``items`` list; each item
        has ``title``, ``author``, ``blurb``, ``source``, and ``thoughts`` (any of which
        may be ``None``).
    """
    return data.READING
