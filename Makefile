build: install
	mkdocs build -f mkdocs.pl.yaml
	mkdocs build -f mkdocs.en.yaml
	
serve:
	./serve.py

install: docs/requirements.txt
	pip install -r docs/requirements.txt

.PHONY: docs/requirements.txt
docs/requirements.txt:
	uv pip compile -q --no-strip-markers -o docs/requirements.txt docs/requirements.in
