ontologyVer=0.3
widoco_url=https://github.com/dgarijo/Widoco/releases/download/v1.4.15/widoco-1.4.15-jar-with-dependencies.jar
scope_css_py=./scope-widoco-css.py

.PHONY: widoco snapshot

widoco: widoco.jar
	mkdir -p widoco
	mkdir -p widoco/doc/sections
	mkdir -p public/doc
	wget -q -P widoco https://reshare-dtc.github.io/reshare-ontology/$(ontologyVer)/ontology.rdf
	java -jar widoco.jar -ontFile widoco/ontology.rdf -outFolder widoco -webVowl -rewriteAll -excludeIntroduction
	cp -R widoco/doc/sections public
	cp -R widoco/doc/resources public
	cp -R widoco/doc/webvowl public
	python3 $(scope_css_py)

widoco.jar:
	wget -q -O widoco.jar $(widoco_url)

clean:
	rm -rf widoco
	rm -rf public/sections
	rm -rf public/resources
	rm -rf public/webvowl

respec-snapshot:
	npx -y respec --src public/index-src.html --out public/index.html --localhost