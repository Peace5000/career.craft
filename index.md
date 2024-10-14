---
layout: default
title: CV Creation Page
---

<h1>Welcome to the CV Creation Page!</h1>
<p>Please enter your details below:</p>

<form id="cvForm">
    <label for="name">Name:</label>
    <input type="text" id="name" required><br><br>

    <label for="email">Email:</label>
    <input type="email" id="email" required><br><br>

    <label for="modules">Science Modules:</label>
    <input type="text" id="modules" placeholder="e.g., Physics, Chemistry" required><br><br>

    <input type="submit" value="Create CV">
</form>

<div id="cvOutput" style="margin-top: 20px;"></div>

<script>
    document.getElementById('cvForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form submission

        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const modules = document.getElementById('modules').value;

        const output = `
            <h2>Your CV</h2>
            <p><strong>Name:</strong> ${name}</p>
            <p><strong>Email:</strong> ${email}</p>
            <p><strong>Science Modules:</strong> ${modules}</p>
            <p>Congratulations! You're a genius! 🎉</p>
        `;
        document.getElementById('cvOutput').innerHTML = output;
    });
</script>
