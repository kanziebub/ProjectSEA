---
layout: default
---

![Logo](https://kanziebub.github.io/ProjectSEA/assets/images/bullet_rev.png)
[Home](https://kanziebub.github.io/ProjectSEA/)

# ProjectSEA Sponsorship Proposal

<!-- PDF container -->
<div id="proposal-page-container">
    <div id="loading" class="loader"></div>
    <div id="pdf-container"></div>
</div>

<script>
  const url = 'https://kanziebub.github.io/ProjectSEA/assets/files/proposal.pdf';

  const container = document.getElementById('pdf-container');
  const loading = document.getElementById('loading');
  const pdfjsLib = window['pdfjs-dist/build/pdf'];

  const containerWidth = container.offsetWidth;

  pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.14.305/pdf.worker.min.js';

  pdfjsLib.getDocument(url).promise.then(function(pdfDoc) {
    // Hide spinner and show PDF container
    loading.style.display = 'none';
    container.style.display = 'block';

    for (let i = 1; i <= pdfDoc.numPages; i++) {
      pdfDoc.getPage(i).then(function(page) {
        const viewport = page.getViewport({ scale: 0.8 });
        const canvas = document.createElement('canvas');
        canvas.height = viewport.height;
        canvas.width = viewport.width;
        container.appendChild(canvas);

        const context = canvas.getContext('2d');
        page.render({ canvasContext: context, viewport: viewport });
      });
    }
  });
</script>


![Logo](https://kanziebub.github.io/ProjectSEA/assets/images/bullet_rev.png)
[Home](https://kanziebub.github.io/ProjectSEA/)
