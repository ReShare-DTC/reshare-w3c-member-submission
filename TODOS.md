## TODOs before FIT Review

### Major

- [x] Specify the authority IRI mechanism: Say what we specify and what not, and give an example how to implement it
  - We need to match IRIs to authoritys
  - Approach in spec:
    - Say that any mechanism fulfilling some requirements can be used
    - Requirements: IRI must be included somewhere (?) in the X.509 certificate, ... (what else?)
    - Could not find an example on this. Our approach probably isn't best practice anyway. Keep this pretty vague.
    - Say that an authority has to have an IRI, and the certificate has to clearly state it is issued for said IRI
    - Authority IRIs should be expressive and re-used to make them interpretable and valuable for the contract partners
      - i.e., a company/division should have one such IRI only and use that, don't randomly generate them
- [x] Refactor DTC verification section to be normative

- [ ] Update ontology

  - See the [README.md](https://git.rwth-aachen.de/i5/factdag/reshare-ontology/-/blob/master/README.md) of the ontology repo
  - Missing: Substitute IRIs by w3id IRIs, (quality control)

- [ ] After finished ontology update
- Update ontology IRIs and JSON-LD throughout document!

- [ ] Rework considerations section

  - Considerations aggregates extension points and some discussion points too verbose for the main part of the specification
  - As of now, only an ad-hoc collection of some text already written before, probably out of context
  - Needs to be reworked

- [ ] Create w3id IRIs for JSON Schemas, the ontology, the JSON-LD context

  - Open [fork](https://github.com/MangelWare/w3id.org), should be submitted as PR after review

- [ ] Resolve issues throughout document

  - [ ] Primer: Heading changes, glue, missing references
  - [ ] DTCs: Missing component overview, wall of text in signature paradigms, missing refs, summarizing statement
  - [ ] Ontology: Bump to v0.3
  - [ ] Before appendix: Summary of abstract

- [ ] Possibly reword the primer and introduction towards accountability, not reliability

- [ ] Write abstract

### Minor

- [ ] Name the venues of cited papers

  - Really? Other submissions (like [this one](https://www.w3.org/Submission/2015/SUBM-wot-model-20150824/)) also don't do this
  - In general, there don't really seem to be best practices for how to do this

- [ ] Review the DTC examples w.r.t. the latest changes

- [x] Verify that the ReSpec configuration fits a member submission (other than specStatus="Member-SUBM")

  - An example source is [here](https://github.com/webofthings/web-thing-model)
    - The used version of respec is deprecated, see [here](https://github.com/w3c/respec/wiki/respec-w3c-common-migration-guide)
  - What is Prof. Decker's/the FIT's W3CID?
    - "For W3C documents, an identifier of the persons’ W3C account. This id can be found in [my profile](https://www.w3.org/users/myprofile) URL that will be redirected to the user’s page; the id appears in the address bar (e.g., https://www.w3.org/users/12345)."
    - [ ] Ask Carlos what to use here
  - I added a modified copyright notice, which is also present in the other member submissions
    - Thereby, the FIT retains its copyright
    - I did this by adding a `<p class="copyright">...</p>` at the start of the body
    - This _seems_ to be best practice, according to [this PR](https://github.com/w3c/respec/pull/2661) (even if the feature is completely undocumented)
  - How to obtain the `submissionCommentNumber`?
    - Needed according to [ReSpec documentation](https://respec.org/docs/#w3c)
    - Just set it to `01`?
  - The SotD text is different from other Member Submissions
    - Could not find information on how to change this
    - Seems to be the default with the new ReSpec template, should be fine
