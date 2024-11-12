import argparse
import os
from typing import Any

import config as cfg
from liquid import Template


def filepath(filename: str, diff: str = "E", *, py_file: bool = True) -> str:
    if diff not in cfg.DIFFICULTY_MAP:
        expected = ", ".join(cfg.DIFFICULTY_MAP)
        msg = f"unrecognized value for diff. expected one of {expected} but got {diff}"
        raise ValueError(msg)

    parent, file_ext = (
        (cfg.PY_FILE_DIR, ".py") if py_file else (cfg.EXPLANATIONS_DIR, ".md")
    )

    return os.path.join(parent, cfg.DIFFICULTY_MAP[diff], f"{filename}{file_ext}")


def get_markdown_text(args: dict[str, Any]) -> str:
    template = Template(cfg.TEMPLATE)

    difficulty = cfg.DIFFICULTY_MAP[args["difficulty"]]

    context = {
        "name": args["name"],
        "number": args["number"],
        "link": args["link"],
        "n_solutions": args["n_solutions"],
        "difficulty": difficulty.capitalize(),
    }

    return template.render(context)


def startproblem(args: dict[str, Any]) -> None:
    difficulty = args["difficulty"]

    name: str = args["name"]
    name = name.replace("(", "")
    name = name.replace(")", "")

    filename = args["destination"] or "_".join(name.lower().split())

    py_path = filepath(filename=filename, diff=difficulty)

    with open(py_path, "w") as _:
        pass

    md_path = filepath(filename=filename, diff=difficulty, py_file=False)

    with open(md_path, "w") as f:
        text = get_markdown_text(args)
        f.write(text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("name", help="name of the problem as shown in leetcode")

    parser.add_argument(
        "number", type=int, help="problem number as counted on leetcode"
    )

    parser.add_argument("link", help="link to the problem on leetcode")

    parser.add_argument(
        "-d",
        "--difficulty",
        choices=list(cfg.DIFFICULTY_MAP.keys()),
        default="E",
        help="difficulty level of the problem",
    )

    parser.add_argument(
        "-ns",
        "--n-sol",
        type=int,
        default=1,
        help="number of solution blocks to include in markdown file",
        dest="n_solutions",
    )

    parser.add_argument(
        "-dest",
        "--destination",
        default="",
        help="filename for the python and markdown files without extension",
    )

    args = parser.parse_args()
    args = vars(args)

    raise SystemExit(startproblem(args))
