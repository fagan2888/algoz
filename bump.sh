cd /Users/pcotton/github/algoz
rm /Users/pcotton/github/algoz/dist/*
python setup.py sdist bdist_wheel
twine upload dist/*
