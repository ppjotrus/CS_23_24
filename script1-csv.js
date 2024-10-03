// Array to hold user data
let userData = [];

// Function to add user data to the array
function addData() {
    // Get input field values
    const firstName = document.getElementById("firstName").value;
    const lastName = document.getElementById("lastName").value;
    const age = document.getElementById("age").value;

    if (firstName && lastName && age) {
        // Add data to the array
        userData.push({
            firstName: firstName,
            lastName: lastName,
            age: age
        });

        // Show added data in output
        document.getElementById("output").innerText = JSON.stringify(userData, null, 2);

        // Clear input fields after adding data
        document.getElementById("firstName").value = "";
        document.getElementById("lastName").value = "";
        document.getElementById("age").value = "";
    } else {
        alert("Please fill in all fields!");
    }
}

// Function to download the array as a CSV file
function downloadCSV() {
    if (userData.length === 0) {
        alert("No data to download!");
        return;
    }

    let csvContent = "data:text/csv;charset=utf-8,";

    // Add CSV header
    csvContent += "First Name,Last Name,Age\n";

    // Add array data to CSV content
    userData.forEach(row => {
        csvContent += `${row.firstName},${row.lastName},${row.age}\n`;
    });

    // Create a link element to trigger the download
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "user_data.csv");

    // Append the link and trigger the download
    document.body.appendChild(link);
    link.click();

    // Clean up the link element
    document.body.removeChild(link);
}
