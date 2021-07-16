import path
import invoke


def get_pylint_args():
    top_path = path.Path(".")
    top_dirs = top_path.dirs()
    for top_dir in top_dirs:
        if top_dir.joinpath("__init__.py").exists():
            yield top_dir
    yield from (x for x in top_path.files("*.py"))


@invoke.task
def pylint(ctx):
    invoke.run("pylint " + " ".join(get_pylint_args()), echo=True)
