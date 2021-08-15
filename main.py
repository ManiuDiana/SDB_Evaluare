from ui.ui import UI
from service.services import Service

service = Service()
ui = UI(service)

ui.run()