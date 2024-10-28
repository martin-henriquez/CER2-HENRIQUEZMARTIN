class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
            
    def __iter__(self):
        for item_id in self.carrito:
            yield self.carrito[item_id]

    def addProduct(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio_total": producto.precio,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["precio_total"] += producto.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    def eliminar(self, producto):
        id  = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def quitar(self, producto): 
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["precio_total"] -= producto.precio
            
            if self.carrito[id]["cantidad"] <= 0: 
                self.eliminar(producto)
            
            self.guardar_carrito()
    
    def cleanner(self):
        self.session["carrito"] = {}
        self.session.modified = True
    
    def get_total(self):
        total = 0
        for item in self.carrito.values():
            total += item["precio_total"]
        return total