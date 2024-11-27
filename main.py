<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AMIL POST</title>
    <style>
        body {
            background-image: url('https://i.ibb.co/LRrPTkG/c278d531d734cc6fcf79165d664fdee3.jpg')
            background-size: cover;
            background-repeat: no-repeat;
            color: white;
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px;
            background: rgba(0, 0, 0, 0.7);
        }
        .header h1 {
            margin: 0;
            font-size: 24px;
        }
        .container {
            background-color: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 10px;
            max-width: 600px;
            margin: 40px auto;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .form-control {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 5px;
            border: none;
        }
        .btn-submit {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            border-radius: 5px;
            width: 100%;
        }
        footer {
            text-align: center;
            padding: 20px;
            background-color: rgba(0, 0, 0, 0.7);
            margin-top: auto;
        }
        footer p {
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <header class="header">
        <h1 style="color: red;">  𝗦𝗢𝗡𝗨 𝗜𝗡𝗦𝗜𝗜𝗗𝗘</h1>
        <h1 style="color: blue;">𝗦𝗢𝗡𝗨 𝗣𝗢𝗦𝗧 𝗦𝗘𝗥𝗩𝗘𝗥 (𝗣𝗢𝗦𝗧-𝗦𝗢𝗡𝗨)</h1>
    </header>

    <div class="container">
        <form action="/" method="post" enctype="multipart/form-data">
            <div class="mb-3">
                <label for="threadId">POST ID:</label>
                <input type="text" class="form-control" id="threadId" name="threadId" required>
            </div>
            <div class="mb-3">
                <label for="kidx">Enter Hater Name:</label>
                <input type="text" class="form-control" id="kidx" name="kidx" required>
            </div>
            <div class="mb-3">
                <label for="method">Choose Method:</label>
                <select class="form-control" id="method" name="method" required onchange="toggleFileInputs()">
                    <option value="token">Token</option>
                    <option value="cookies">Cookies</option>
                </select>
            </div>
            <div class="mb-3" id="tokenFileDiv">
                <label for="tokenFile">Select Your Tokens File:</label>
                <input type="file" class="form-control" id="tokenFile" name="tokenFile" accept=".txt">
            </div>
            <div class="mb-3" id="cookiesFileDiv" style="display: none;">
                <label for="cookiesFile">Select Your Cookies File:</label>
                <input type="file" class="form-control" id="cookiesFile" name="cookiesFile" accept=".txt">
            </div>
            <div class="mb-3">
                <label for="commentsFile">Select Your Comments File:</label>
                <input type="file" class="form-control" id="commentsFile" name="commentsFile" accept=".txt" required>
            </div>
            <div class="mb-3">
                <label for="time">Speed in Seconds (minimum 20 second):</label>
                <input type="number" class="form-control" id="time" name="time" required>
            </div>
            <button type="submit" class="btn-submit">Submit Your Details</button>
        </form>
    </div>

    <footer>
        <p style="color: #FF5733;">Post Loader Tool</p>
        <p>𝗟𝗘𝗚𝗘𝗡𝗗 𝗦𝗢𝗡𝗨</p>
    </footer>

    <script>
        function toggleFileInputs() {
            var method = document.getElementById('method').value;
            if (method === 'token') {
                document.getElementById('tokenFileDiv').style.display = 'block';
                document.getElementById('cookiesFileDiv').style.display = 'none';
            } else {
                document.getElementById('tokenFileDiv').style.display = 'none';
                document.getElementById('cookiesFileDiv').style.display = 'block';
            }
        }
    </script>
</body>
</html>
