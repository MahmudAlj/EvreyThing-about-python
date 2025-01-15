# Create an Activity Diagram for Task 3 of the hotel system project
from graphviz import Digraph

# Initialize the graph
dot = Digraph(format="png", comment="Hotel System Activity Diagram for Task 3")

# Define nodes
dot.node("Start", "Başlangıç\nMüşteri rezervasyon sistemine giriş yapar", shape="ellipse")
dot.node("Login", "Giriş Yapma", shape="rectangle")
dot.node("SelectDates", "Giriş ve çıkış tarihlerini seçer", shape="rectangle")
dot.node("CheckAvailability", "Sistem uygun odaları kontrol eder", shape="diamond")
dot.node("RoomAvailable", "Oda mevcut", shape="rectangle")
dot.node("SelectRoom", "Oda tipini ve ek hizmetleri seçer", shape="rectangle")
dot.node("EnterPayment", "Ödeme bilgilerini girer", shape="rectangle")
dot.node("ConfirmBooking", "Rezervasyonu onaylar", shape="rectangle")
dot.node("SaveBooking", "Sistem rezervasyonu kaydeder", shape="rectangle")
dot.node("SendConfirmation", "Müşteriye onay bilgisi gönderir", shape="rectangle")
dot.node("End", "Bitiş\nRezervasyon işlemi tamamlanır", shape="ellipse")

# Define edges
dot.edge("Start", "Login")
dot.edge("Login", "SelectDates")
dot.edge("SelectDates", "CheckAvailability")
dot.edge("CheckAvailability", "RoomAvailable", label="Evet")
dot.edge("RoomAvailable", "SelectRoom")
dot.edge("SelectRoom", "EnterPayment")
dot.edge("EnterPayment", "ConfirmBooking")
dot.edge("ConfirmBooking", "SaveBooking")
dot.edge("SaveBooking", "SendConfirmation")
dot.edge("SendConfirmation", "End")
dot.edge("CheckAvailability", "End", label="Hayır")

# Save and render the diagram
output_path = "/mnt/data/hotel_task3_activity_diagram"
dot.render(output_path, view=False)

output_path +
