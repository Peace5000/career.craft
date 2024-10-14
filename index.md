---
layout: default
title: Welcome to My CV Creation Page
---

<h1>Welcome!</h1>
<p>Please enter your details below:</p>

<form id="cvForm">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required><br><br>

    <label for="modules">Science Modules:</label>
    <input type="text" id="modules" name="modules" required><br><br>

    <label for="skills">Skills:</label>
    <input type="text" id="skills" name="skills" required><br><br>

    <input type="submit" value="Submit">
</form>

<script>
    document.getElementById('cvForm').addEventListener('submit', function(event) {
        event.preventDefault();
        
        const name = document.getElementById('name').value;
        const modules = document.getElementById('modules').value;
        const skills = document.getElementById('skills').value;

        // Create the CV page dynamically
        const cvContent = `<h1>${name}'s CV</h1>
        <h2>Science Modules</h2>
        <p>${modules}</p>
        <h2>Skills</h2>
        <p>${skills}</p>
        <h2>Congratulations!</h2>
        <p>Wow, you're a genius! 🎉</p>`;

        // Create a new HTML page and write the content
        const newWindow = window.open();
        newWindow.document.write(cvContent);
        newWindow.document.close();
    });
</script>
