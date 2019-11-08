set -eux
cookiecutter --no-input .
pushd name-of-the-project
make pip-compile
# The generated requirements file is initially owned by root, so update ownership.
sudo chown -R travis .
make network build qa
popd
