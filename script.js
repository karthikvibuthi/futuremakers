const submitButton = document.getElementById("submit");
const outputList = document.getElementById("output");

function showSection(sectionId) {
    // Hide all sections
    const sections = ["InterviewSummary", "assesment"];
    sections.forEach((section) => {
        document.getElementById(section).style.display = "none";
    });

    // Show the requested section
    document.getElementById(sectionId).style.display = "block";
}
// Show the Interview Summary section by default
showSection("InterviewSummary");

document.getElementById('questions-form').addEventListener("submit", async function (event) {
    event.preventDefault(); // Prevent the form from refreshing the page
  
    // Get the input values
    const Q1 = document.getElementById('Q1').value;
    const Q2 = document.getElementById('Q2').value;
    const Q3 = document.getElementById('Q3').value;
    const Q4 = document.getElementById('Q4').value;
    const Q5 = document.getElementById('Q5').value;
    const Q6 = document.getElementById('Q6').value;
    const Q7 = document.getElementById('Q7').value;

    // Display the responses in the respective <p> tags
    document.getElementById('Q1Response').textContent = `User wants to spend ${Q1} minutes on this activity.`;
    document.getElementById('Q2Response').textContent = `Learners belong to ${Q2} grade`;
    document.getElementById('Q3Response').textContent = `Learning environment is specified as: ${Q3}.`;
    document.getElementById('Q4Response').textContent = `Confidence level in hands-on projects is: ${Q4} out of 5.`;
    document.getElementById('Q5Response').textContent = `Include an assessment? ${Q5}.`;
    document.getElementById('Q6Response').textContent = `Teach science of flight while building the model? ${Q6}.`;
    document.getElementById('Q7Response').textContent = `Learners collaborating in groups for the extension project? ${Q7}.`;
    document.getElementById('userResponses').style.display = 'block';

    // Prepare the data to send to the API
    const interviewAnswers = {
        Q1, Q2, Q3, Q4, Q5, Q6, Q7
    };

    try {
        // Make the API call
        const response = await fetch("https://karthikvibuthiportfolio.com/futuremakers/lesson-plan", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ "interview-answers": interviewAnswers })
        });

        // Parse and handle the response
        if (response.ok) {
            const result = await response.json();
            console.log("API Response:", result);
            outputList.textContent = `API Response: ${JSON.stringify(result)}`;
        } else {
            console.error("Error from API:", response.statusText);
            outputList.textContent = `Error from API: ${response.statusText}`;
        }
    } catch (error) {
        console.error("API Call Failed:", error);
        outputList.textContent = `API Call Failed: ${error.message}`;
    }
});
