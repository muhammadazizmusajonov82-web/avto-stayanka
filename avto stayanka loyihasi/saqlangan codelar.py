# <!-- files: cars/templates/dashboard.html faylining eng yuqori qismini mana shu kodga almashtiring -->
# <!DOCTYPE html>
# <html lang="uz">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Avto Turargoh Tizimi</title>
#     <!-- TO'G'RILANGAN BOOTSTRAP LINKI - Endi dizayn to'liq ishlaydi -->
#     <link href="https://jsdelivr.net" rel="stylesheet">
#     <style>
#         body { background-color: #f3f4f6; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
#
#         /* 🏢 CHAP BURCHAK: Monitor qismini 15% gacha kichraytirdik va ichki masofani 15px qildik */
#         .sidebar { background: #1e293b; color: white; min-height: 100vh; padding: 15px; position: fixed; width: 15%; top: 0; left: 0; z-index: 1000; box-shadow: 4px 0 10px rgba(0,0,0,0.1); }
#
#         /* 🚗 O'NG TOMON: Bo'shliqni 15% qilib mosladik va o'ng tomon 85% gacha kengaydi */
#         .main-content { margin-left: 15%; width: 85%; padding: 30px; }
#
#         .card-custom { border: none; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); background-color: #ffffff; }
#         .badge-plate { background-color: #e2e8f0; color: #1e293b; font-weight: bold; border: 2px solid #cbd5e1; border-radius: 6px; padding: 6px 12px; letter-spacing: 1px; }
#         .monitor-card { border-radius: 10px; padding: 15px; text-center; border: none; margin-bottom: 15px; }
#     </style>
#
# </head>
# <body>
#
# <div class="container-fluid p-0">
#     <div class="d-flex">
#
#         <!-- 🧭 CHAP BURCHAK: Ixcham Monitor paneli -->
#         <div class="sidebar d-flex flex-column justify-content-between">
#             <div>
#                 <h4 class="text-center fw-bold mb-4 text-warning">🅿️ STAYANKA</h4>
#                 <hr class="border-secondary">
#
#                 <div class="card bg-success text-white text-center monitor-card shadow-sm">
#                     <span class="text-uppercase small fw-bold">Bo'sh Joylar</span>
#                     <h1 class="display-5 fw-bold my-1">{{ free_spaces }}</h1>
#                     <small class="opacity-75">Maks: 200</small>
#                 </div>
#
#                 <div class="card bg-primary text-white text-center monitor-card shadow-sm">
#                     <span class="text-uppercase small fw-bold">Band Joylar</span>
#                     <h1 class="display-5 fw-bold my-1">{{ current_count }}</h1>
#                 </div>
#             </div>
#
#             <div>
#                 <hr class="border-secondary">
#                 <a href="{% url 'logout' %}" class="btn btn-outline-danger w-100 fw-bold py-2">🚪 Tizimdan Chiqish</a>
#             </div>
#         </div>
#
#         <!-- 🚗 O'NG TOMON: Chiroyli va kengaytirilgan qism -->
#         <div class="main-content">
#
#             <!-- Yuqori banner -->
#             <div class="p-4 rounded mb-4 card-custom border-start border-primary border-5 d-flex justify-content-between align-items-center">
#                 <div>
#                     <h2 class="text-dark fw-bold m-0">👋 Salom, Avtoturargohga Xush Kelibsiz!</h2>
#                     <p class="text-muted mt-1 mb-0">Tizim avtomatik ravishda 1-soatni tekin, keyingi har bir soatni 1,500 so'mdan hisoblaydi.</p>
#                 </div>
#                 <span class="badge bg-soft-primary text-primary px-3 py-2 rounded-pill fw-bold" style="background-color: #e0e7ff;">Online Boshqaruv</span>
#             </div>
#
#             <!-- Tizim bildirishnomasi (Yashil/Qizil xabarlar) -->
#             {% if messages %}
#                 {% for message in messages %}
#                     <div class="alert {% if message.tags == 'error' %}alert-danger{% else %}alert-success{% endif %} alert-dismissible fade show shadow-sm" role="alert">
#                         <strong>🛡️ Tizim:</strong> {{ message }}
#                         <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Yopish"></button>
#                     </div>
#                 {% endfor %}
#             {% endif %}
#
#           <!-- ... tepadagi kodlar ... -->
# <div class="row">
#
#     <!-- 📥 MANA SHU YERDA SIZNING KODINGIZ TURIBDI -->
#     <div class="col-lg-5 mb-4">
#         <div class="card p-4 card-custom bg-white border border-success border-3">
#             <h3 class="fw-bold mb-4 text-success">📝 Yangi Avto Kirishi</h3>
#             <form action="{% url 'park_car' %}" method="post">
#                 {% csrf_token %}
#                 <div class="mb-4">
#                     <label class="form-label fw-bold text-dark fs-5">Mashina Raqami:</label>
#                     <input type="text" name="plate_number" class="form-control form-control-lg text-uppercase fw-bold text-center bg-light border-secondary p-3 fs-4" placeholder="01 A 123 AA" required>
#                 </div>
#                 <div class="mb-4">
#                     <label class="form-label fw-bold text-dark fs-5">Mashina Rusumi:</label>
#                     <input type="text" name="car_model" class="form-control form-control-lg bg-light border-secondary p-3 fs-5" placeholder="Gentra, Cobalt, Nexia" required>
#                 </div>
#                 <button type="submit" class="btn btn-primary btn-lg w-100 shadow fw-bold py-3 fs-4">🚀 Stayankaga kiritish</button>
#             </form>
#         </div>
#     </div>
#
#     <!-- 📋 O'ng tomondagi ro'yxat qismi (col-lg-7) ... -->
# <!-- ... pastdagi kodlar ... -->
#
#
#
#                 <!-- 📋 O'NG BURCHAK: Kirgan avtomashinalar ro'yxati va Search -->
#                 <div class="col-lg-7">
#                     <div class="card p-4 card-custom">
#
#                         <!-- 🔍 YUQORI QISM: Zamonaviy Search qidiruv tizimi -->
#                         <div class="mb-4">
#                             <form method="get" action="">
#                                 <div class="input-group">
#                                     <input type="text" name="q" class="form-control form-control-lg border-secondary-subtle" placeholder="Raqam yoki rusum bo'yicha qidirish..." value="{{ search_query }}">
#                                     <button class="btn btn-dark px-4" type="submit">🔍 Qidiruv</button>
#                                     {% if search_query %}
#                                         <a href="{% url 'parking_dashboard' %}" class="btn btn-outline-secondary d-flex align-items-center">Tozalash</a>
#                                     {% endif %}
#                                 </div>
#                             </form>
#                         </div>
#
#                         <h4 class="fw-bold mb-3 text-secondary">🚘 Kirgan avtomashinalar ro'yxati</h4>
#                         <div class="table-responsive" style="max-height: 400px; overflow-y: auto;">
#                             <table class="table table-hover align-middle">
#                                 <thead class="table-light sticky-top">
#                                     <tr>
#                                         <th>Raqami</th>
#                                         <th>Rusumi</th>
#                                         <th class="text-center">Amal</th>
#                                     </tr>
#                                 </thead>
#                                 <tbody>
#                                     {% for car in cars %}
#                                     <tr>
#                                         <td><span class="badge-plate">{{ car.plate_number }}</span></td>
#                                         <td><span class="fw-bold text-dark">{{ car.car_model }}</span></td>
#                                         <td class="text-center">
#                                             <!-- Kichik bo'lim tugmasi -->
#                                             <button type="button" class="btn btn-outline-info btn-sm fw-bold px-3 me-1" data-bs-toggle="modal" data-bs-target="#carModal{{ car.id }}">
#                                                 👁️ Batafsil
#                                             </button>
#                                             <a href="{% url 'unpark_car' car.id %}" class="btn btn-warning btn-sm fw-bold px-3">Chiqarish</a>
#                                         </td>
#                                     </tr>
#
#                                     <!-- 👁️ MODAL OYNA: Ichiga kirganda qancha vaqt turganini ko'rsatadi -->
#                                     <div class="modal fade" id="carModal{{ car.id }}" tabindex="-1" aria-hidden="true">
#                                         <div class="modal-dialog modal-dialog-centered">
#                                             <div class="modal-content border-0 shadow-lg" style="border-radius: 16px;">
#                                                 <div class="modal-header bg-dark text-white border-0" style="border-top-left-radius: 16px; border-top-right-radius: 16px;">
#                                                     <h5 class="modal-title fw-bold">🚗 Avtomobil ma'lumotlari</h5>
#                                                     <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
#                                                 </div>
#                                                 <div class="modal-body p-4">
#                                                     <div class="mb-3 d-flex justify-content-between">
#                                                         <span class="text-muted">Mashina raqami:</span>
#                                                         <span class="badge-plate">{{ car.plate_number }}</span>
#                                                     </div>
#                                                     <div class="mb-3 d-flex justify-content-between">
#                                                         <span class="text-muted">Mashina rusumi:</span>
#                                                         <span class="fw-bold text-dark">{{ car.car_model }}</span>
#                                                     </div>
# <!-- files: cars/templates/dashboard.html faylining aynan o'sha qismidan boshlab oxirigacha almashtiring -->
#
#                                                     <div class="mb-3 d-flex justify-content-between">
#                                                         <span class="text-muted">Kirgan vaqti:</span>
#                                                         <span class="fw-bold text-secondary">{{ car.arrival_time|date:"H:i (d-F Y)" }}</span>
#                                                     </div>
#                                                     <hr class="my-4">
#                                                     <div class="p-3 bg-light rounded-3 text-center border">
#                                                         <span class="text-uppercase small fw-bold text-muted d-block mb-1">Stayankada qolgan davomiyligi:</span>
#                                                         <h3 class="text-danger fw-bold m-0">{{ car.get_duration_string }}</h3>
#                                                     </div>
#                                                 </div>
#                                                 <div class="modal-footer border-0 bg-light-subtle" style="border-bottom-left-radius: 16px; border-bottom-right-radius: 16px;">
#                                                     <button type="button" class="btn btn-secondary px-4" data-bs-dismiss="modal">Yopish</button>
#                                                     <a href="{% url 'unpark_car' car.id %}" class="btn btn-warning fw-bold px-4">Chiqarish & Hisoblash</a>
#                                                 </div>
#                                             </div>
#                                         </div>
#                                     </div>
#
#                                     {% empty %}
#                                     <tr>
#                                         <td colspan="3" class="text-center text-muted py-4">Hech qanday mashina topilmadi.</td>
#                                     </tr>
#                                     {% endfor %}
#                                 </tbody>
#                             </table>
#                         </div>
#                     </div>
#                 </div>
#             </div> <!-- row end -->
#         </div>
#     </div>
# </div>
#
# <!-- Bootstrap JS Bundle -->
# <script src="https://jsdelivr.net"></script>
# </body>
# </html>
#
