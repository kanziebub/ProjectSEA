---
layout: default
---

![Logo](https://kanziebub.github.io/ProjectSEA/assets/images/bullet_rev.png)
[Home](https://kanziebub.github.io/ProjectSEA/)

# ProjectSEA Sponsorship Proposal

<div id="pdf-container" style="width: 100%; height: 100%; min-height: 600px; max-width: 600px; border: 1px solid #ccc;"></div>

<script>
  const url = 'https://kanziebub.github.io/ProjectSEA/assets/files/proposal.pdf';

  const container = document.getElementById('pdf-container');
  const pdfjsLib = window['pdfjs-dist/build/pdf'];

  pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.14.305/pdf.worker.min.js';

  pdfjsLib.getDocument(url).promise.then(function(pdfDoc) {
    for (let i = 1; i <= pdfDoc.numPages; i++) {
      pdfDoc.getPage(i).then(function(page) {
        const scale = container.offsetWidth / viewport.width;
        const viewport = page.getViewport({ scale: scale });
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
