import argparse
import sys


def main(input_file, pipeline_break):
    try:
        with open(input_file, "r") as file:
            return_code = int(pipeline_break)
            for line in file:
                stripped_line = line.strip()

                # Skip the header lines
                if stripped_line.startswith("usage-policy") or stripped_line.startswith(
                    "------------"
                ):
                    continue

                # usage-policy is the first column
                usage_policy = stripped_line.split()[0]

                # Check if the usage-policy is UNDEFINED, needs-review, or deny
                if usage_policy == "UNDEFINED":
                    print(f"Found a license that is undefined: {stripped_line}")
                elif usage_policy == "needs-review":
                    print(f"Found a license needing review: {stripped_line}")
                elif usage_policy == "deny":
                    print(f"Found a license which is denied: {stripped_line}")
                    return_code = 1
    except FileNotFoundError:
        print(f"File not found: {input_file}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    sys.exit(return_code)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("--pipelinebreak", "-p", type=str)
    args = parser.parse_args()
    main(args.filename, args.pipelinebreak == "true")
