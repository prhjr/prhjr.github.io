// Ensure jsPDF is available globally
var jsPDF = window.jspdf;

// Function to capture the entire HTML content and save it as a PDF
function saveAsPDF() {
    // Check if jsPDF is defined
    if (jsPDF && jsPDF.jsPDF) {
        // Create a new jsPDF instance
        var pdf = new jsPDF.jsPDF();

        // Function to add HTML content to PDF
        function addHtmlToPDF(element, callback) {
            html2canvas(element, {
                onrendered: function (canvas) {
                    var imgData = canvas.toDataURL('image/png');
                    pdf.addImage(imgData, 'PNG', 10, 10);
                    callback();
                }
            });
        }

        // Add HTML content to PDF
        addHtmlToPDF(document.body, function () {
            // Save the PDF and trigger the download
            pdf.save('webpage-content.pdf');
        });
    } else {
        console.error('jsPDF is not defined. Make sure the library is loaded.');
    }
}

// Attach the click event to the button
$('#downloadBtn').on('click', function () {
    saveAsPDF();
});
