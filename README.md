<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Do‘kon</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: 'Segoe UI', sans-serif;
      background: url('https://100k.uz/static/media/bg.2be69e6b.jpg') no-repeat center center fixed;
      background-size: cover;
      color: white;
    }
    .container {
      padding: 20px;
    }
    h1 {
      text-align: center;
      margin-bottom: 30px;
    }
    .product {
      background: rgba(0, 0, 0, 0.6);
      border-radius: 15px;
      margin-bottom: 20px;
      padding: 15px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .product img {
      max-width: 100%;
      border-radius: 10px;
    }
    .product h2 {
      margin: 10px 0 5px 0;
    }
    .product p {
      margin: 0 0 10px 0;
    }
    button {
      padding: 10px 20px;
      background: #00b894;
      color: white;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      font-size: 16px;
    }
    button:hover {
      background: #019874;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>🛒 Do‘kon</h1>

    <div class="product">
      <img src="https://via.placeholder.com/300x200" alt="Mahsulot">
      <h2>Mahsulot 1</h2>
      <p>Mahsulot haqida qisqacha ma'lumot</p>
      <p><strong>💵 Narx: 50 000 so'm</strong></p>
      <button onclick="addToCart(1)">➕ Savatga qo‘shish</button>
    </div>

    <div class="product">
      <img src="https://via.placeholder.com/300x200" alt="Mahsulot">
      <h2>Mahsulot 2</h2>
      <p>Ikkinchi mahsulot haqida</p>
      <p><strong>💵 Narx: 100 000 so'm</strong></p>
      <button onclick="addToCart(2)">➕ Savatga qo‘shish</button>
    </div>
  </div>

  <script>
    function addToCart(productId) {
      Telegram.WebApp.sendData(JSON.stringify({
        action: 'add_to_cart',
        id: productId
      }));
    }

    window.onload = () => {
      Telegram.WebApp.ready();
    };
  </script>
</body>
</html>
