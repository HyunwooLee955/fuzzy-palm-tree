import nox


@nox.session(reuse_venv=True)
def docs(session: nox.Session) -> None:
    """
    Build the docs. Pass --non-interactive to avoid serving. First positional argument is the target directory.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-b", dest="builder", default="html", help="Bild target (default: html)"
    )
    parser.add_argument("output", nargs="?", help="Output directory")
    args, posargs = parser.parse_know_args(session.posargs)
    serve = args.builder == "html" and session.interactive

    session.install("-e.[docs]", "sphinx-autobuild")

    shared_args = (
        "-n",  # nitpicky mode
        "-T",  # full tracebacks
        f"-b={args.builder}",
        "docs",
        args.output or f"docs/_build/{args.builder}",
        *posargs,
    )

    if serve:
        session.run("sphinx-autobild", "--open-browser", *shared_args)
    else:
        session.run("sphinx-build", "--keep-going", *shared_args)


@nox.session
def build_api_docs(session: nox.Session) -> None:
    """
    Build (regenerate) API docs.
    """

    session.install("sphinx")
    session.run(
        "sphinx-apidoc",
        "-o",
        "docs/api/",
        "--module-first",
        "--no-toc",
        "--force",
        "src/example",
    )
