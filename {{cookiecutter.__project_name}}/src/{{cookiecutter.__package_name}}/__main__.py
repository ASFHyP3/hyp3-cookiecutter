"""{{ cookiecutter.process_type }} processing for HyP3."""

import logging
from argparse import ArgumentParser

from hyp3lib.aws import upload_file_to_s3

from {{ cookiecutter.__package_name }}.process import {{ cookiecutter.__process_name }}


def main() -> None:
    """HyP3 entrypoint for {{ cookiecutter.__package_name }}."""
    parser = ArgumentParser()
    parser.add_argument('--bucket', help='AWS S3 bucket HyP3 for upload the final product(s)')
    parser.add_argument('--bucket-prefix', default='', help='Add a bucket prefix to product(s)')

    # TODO: Your arguments here
    parser.add_argument('--greeting', default='Hello world!', help='Write this greeting to a product file')

    args = parser.parse_args()

    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO
    )

    product_file = {{ cookiecutter.__process_name }}(
        greeting=args.greeting,
    )

    if args.bucket:
        upload_file_to_s3(product_file, args.bucket, args.bucket_prefix)


if __name__ == '__main__':
    main()
