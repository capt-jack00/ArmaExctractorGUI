import argparse
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
from pathlib import Path
import sys

def main():
    parser = argparse.ArgumentParser(description="This program extracts mod id's from a html file to txt file")
    parser.add_argument("--input", type=str, required=True, help="Provides input modpack file")
    parser.add_argument("--output", type=str, required=True, help="Provides output .txt file")

    args = parser.parse_args()
    inputPath = Path(args.input)
    outputPath = Path(args.output)

    if inputPath.suffix == ".html":
        with open(args.input, "r", encoding="utf-8") as file:
            html_content = file.read()
    
    else:
        print("Incorrect input file extension! Please provide an HTML file!", file=sys.stderr)
        sys.exit(1)

    soup = BeautifulSoup(html_content, "html.parser")

    if outputPath.suffix == ".txt":
        with open(args.output, "a", encoding="utf-8") as f:
            for a in soup.find_all("a"):
                href = a.get("href")
                if href:
                    parsed_url = urlparse(href)
                    query_params = parse_qs(parsed_url.query)
                    id_value = query_params.get("id", [None])[0]
                    print(id_value)
                    f.write(id_value + "\n") 
    else:
        print("Invalid output file extension! Please provide a txt file!", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
