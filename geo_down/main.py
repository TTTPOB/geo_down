import argparse
from typing import List

import httpx


def get_link(acc: str) -> str:
    return f"https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={acc}&targ=self&form=text&view=full"


def get_supp_file(content: str) -> List[str]:
    supp = []
    for l in content.split("\n"):
        if l.startswith("!Series_supplementary_file"):
            supp.append(l.split("=")[1].strip())
    return supp


def get_filename(url: str) -> str:
    return url.split("/")[-1]


def get_aria2c(url: str) -> str:
    filename = get_filename(url)
    return f"{url}\n  out={filename}"


def cli(acc: str):
    link = get_link(acc)
    content = httpx.get(link).text
    supp_files = get_supp_file(content)
    aria2c_input_file = "\n".join([get_aria2c(url) for url in supp_files])
    print(aria2c_input_file)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("acc", help="GEO accession number")
    args = parser.parse_args()
    cli(args.acc)


if __name__ == "__main__":
    main()
