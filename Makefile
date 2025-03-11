serve-en:
	uv run mkdocs serve \
		--config-file mkdocs.en.yaml \
		--watch ./src/en \
		--watch ./overrides \
		--watch ./mkdocs.en.yaml \
		--watch ./base.yaml

serve-pl:
	uv run mkdocs serve \
		--config-file mkdocs.pl.yaml \
		--watch ./src/pl \
		--watch ./overrides \
		--watch ./mkdocs.pl.yaml \
		--watch ./base.yaml

build: install
	uv run mkdocs build -f mkdocs.pl.yaml
	uv run mkdocs build -f mkdocs.en.yaml
	
serve:
	uv run python ./serve.py
