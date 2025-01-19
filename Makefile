serve-en:
	mkdocs serve \
		--config-file mkdocs.en.yaml \
		--watch ./src/en \
		--watch ./overrides \
		--watch ./mkdocs.en.yaml \
		--watch ./base.yaml

serve-pl:
	mkdocs serve \
		--config-file mkdocs.pl.yaml \
		--watch ./src/pl \
		--watch ./overrides \
		--watch ./mkdocs.pl.yaml \
		--watch ./base.yaml

build: install
	mkdocs build -f mkdocs.pl.yaml
	mkdocs build -f mkdocs.en.yaml
	
serve:
	./serve.py

install: src/requirements.txt
	pip install -r src/requirements.txt

.PHONY: src/requirements.txt
src/requirements.txt:
	uv pip compile -q --no-strip-markers -o src/requirements.txt src/requirements.in
