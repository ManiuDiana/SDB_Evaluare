from ui import UI
from services import Service

service = Service()
ui = UI(service)

ui.run()