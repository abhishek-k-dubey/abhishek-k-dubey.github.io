# Abhishek K. Dubey — personal website

A responsive professional portfolio for pharma employers and executive MBA reviewers. Plain HTML, CSS and JavaScript; no installation, build step, database or paid service is required.

## Preview

Unzip the package and open `index.html`. Keep the `assets` folder beside it. The separate `Abhishek-Dubey-Website-Preview.html` download embeds all assets for a convenient single-file preview.

## Publish with GitHub Pages

1. Sign in to GitHub in your own browser.
2. Create a public repository named `YOUR-USERNAME.github.io`, using your exact GitHub username. You can also use a project repository such as `abhishek-dubey`.
3. Choose **Add file → Upload files** and upload the contents of this extracted package. Place `index.html` at the repository root, with `assets` beside it. Upload the extracted files, not the ZIP.
4. Commit the files to `main`.
5. In **Settings → Pages**, select **Deploy from a branch**, then **main** and **/(root)**, and save.
6. The Pages settings screen displays the published URL after deployment completes. Subsequent commits update the site.

Relative asset paths support both user and project repositories. See GitHub's [site creation instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site) and [publishing-source instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

No repository or public deployment has been created for this package.

## Content and navigation

Six main views provide a short first read and access to seven detailed projects:

| View | Purpose |
| --- | --- |
| Overview | Current role, leadership scope, three contributions and future direction |
| Leadership & strategy | Two contextual decisions, mentoring and development priorities |
| Selected work | Clinical development, evidence strategy and biomedical AI projects |
| Career & education | Professional progression, credentials and a brief personal perspective |
| Publications | Selected papers and an expandable bibliography |
| Contact | Email, LinkedIn and CV |

Scientific methods, figures and numerical results sit inside closed disclosure sections. The development diagram shows a simple forward sequence. Case studies retain the context and limits needed to interpret the findings.

Direct links can target a page or specific section, such as `#case-dose`, `#case-protocol`, `#case-seamless`, `#decision-dose` or `#development-vision`. Browser Back/Forward, keyboard navigation, mobile navigation and project filters are supported. Without JavaScript, all sections remain readable.

## Editing

| File | Purpose |
| --- | --- |
| `index.html` | Website content and section structure |
| `assets/styles.css` | Typography, colors, spacing and responsive layouts |
| `assets/site.js` | Navigation, filters and menu behavior |
| `assets/abhishek-dubey.jpg` | Portrait |
| `assets/Abhishek-K-Dubey-CV.pdf` | Downloadable public CV |
| `tools/make_development_diagram.py` | Editable desktop and mobile pathway diagrams |
| `tools/make_figures.py` | Scientific figure generation |

Replace the portrait or CV using the same filename to retain existing links. Run `python3 tools/make_development_diagram.py` to regenerate the pathway SVGs; it uses the Python standard library. Scientific figure generation requires its plotting dependencies.

## Evidence and editorial principles

- The overview establishes current responsibility, selected contributions and direction. Detailed professional decisions appear once, with study-specific context.
- The TNBC dose-learning example is an individual study decision. It does not establish a default Phase 2 sample size. Research simulations are separately labeled and should not be interpreted as patient outcomes.
- The combination protocol amendment is being implemented. The site does not imply completed implementation, regulatory approval, market leadership or achieved financial returns.
- The published dose framework is used in clinical studies. This statement does not imply prospective validation of every research extension.
- Master-versus-separate protocol outputs are illustrative model estimates. Architecture preferences depend on program assumptions; modeled cost differences are not realized savings.
- Biomedical AI findings are research results. Potential applications are distinguished from demonstrated clinical utility.
- Career scope and mentoring experience reflect the author's CV and subsequent clarifications. No budget ownership, direct-report counts or MBA enrollment are inferred.

Selected scientific references:

- Dose selection: Chakraborty, Dubey, Kumar & Chan (2026), [DOI 10.1080/19466315.2026.2668381](https://doi.org/10.1080/19466315.2026.2668381).
- Master protocols: *Master versus Separate Protocols in Oncology: A Quantitative Decision Framework*, Naishu Kui, Abhishek Dubey and Biraj Guha; author-provided research manuscript. Journal publication is not claimed.
- NCI pathology: author-provided Multitask-TwoScale-HENet manuscript by Abhishek Dubey and Peng Jiang. The four tissue-density panels are original manuscript extracts, not generated illustrations. Clinical biomarker validation is not established.
- Chest X-ray analysis: Haque et al. (2023), [full article](https://pmc.ncbi.nlm.nih.gov/articles/PMC10403240/).
- Deformation-field inversion: Dubey et al. (2018), [full article](https://pmc.ncbi.nlm.nih.gov/articles/PMC6097910/).

Supplied manuscripts, slide decks and internal planning materials are not bundled for download. The public CV omits a home street address and telephone number. Citation totals and h-index are not displayed because current values were not verified.

## Checks for this revision

Content, section links, local assets, disclosure defaults, navigation behavior and archive integrity are checked. The desktop and mobile pathway SVGs are visually inspected after rendering. These checks do not constitute browser UI testing.
