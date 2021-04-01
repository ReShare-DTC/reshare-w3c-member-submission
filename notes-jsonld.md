### Notes

- Common markups:

  - `<code>` for names/variables/...
  - `<dfn>` for definitions (sometimes with `data-cite` attribute to cite a spec)

- Use `dl`,`<dt>` and `<dd>` for descriptions!

- [Inclusions and Transformations](https://respec.org/docs/#inclusions-transformations):

  - Include other HTML with the `data-include` or `data-include-replace` attributes!
  - The `data-transform` can be used to apply JS functions to elements (separated by whitespaces)

- Inline notes can be done as `span.note`

- `notoc` class on sections to exclude from the TOC. Alternatively, specify a `maxTocLevel` config option.

- Use [pluralization](https://respec.org/docs/#pluralize)? (For verbs especially)

- `remove` class to remove on build time (e.g., for scripts)

- Convention: use `h2` for every section depth, ReSpec changes it according to the actual depth

- Example figure:

```html
<figure id="fig-linked-data-graph" style="text-align:center">
  <!-- Source for this file is at https://docs.google.com/drawings/d/1_bRm1d9hTTqAqv5q8KEBzI47HxAUrbceA0EE5APh8hA/edit?usp=sharing -->
  <object
    data="linked-data-graph.svg"
    style="width: 75%"
    type="image/svg+xml"
    aria-describedby="fig-linked-data-graph-alt"
  >
    <p id="fig-linked-data-graph-alt">
      The image depicts a linked data dataset with a default graph and two named
      graphs.
    </p>
  </object>
  <figcaption>
    An illustration of a linked data dataset.<br />
    A
    <a href="#fig-linked-data-graph-descr"
      >description of the linked data dataset diagram</a
    >
    is available in the Appendix. Image available in
    <a href="linked-data-graph.svg" title="SVG image of a linked data dataset">
      <abbr title="Scalable Vector Graphics">SVG</abbr>
    </a>
    and
    <a title="PNG image of a linked data dataset" href="linked-data-graph.png">
      <abbr title="Portable Network Graphics">PNG</abbr>
    </a>
    formats.
  </figcaption>
</figure>
```
