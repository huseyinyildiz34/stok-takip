import gradio as gr

# Stok veri yapısı (örnek olarak bir sözlük kullanıyoruz)
inventory = {}

# Ürün ekleme fonksiyonu
def add_product(product_name, quantity):
    if product_name in inventory:
        return f"'{product_name}' zaten mevcut. Lütfen stok güncelleme işlemini kullanın."
    inventory[product_name] = quantity
    return f"'{product_name}' eklendi. Miktar: {quantity}"

# Stok güncelleme fonksiyonu
def update_stock(product_name, quantity_change):
    if product_name not in inventory:
        return f"'{product_name}' bulunamadı. Lütfen önce ürünü ekleyin."
    inventory[product_name] += quantity_change
    return f"'{product_name}' güncellendi. Yeni miktar: {inventory[product_name]}"

# Stok görüntüleme fonksiyonu
def view_inventory():
    if not inventory:
        return "Stokta ürün yok."
    stock_list = "\n".join([f"{product}: {quantity}" for product, quantity in inventory.items()])
    return f"Stok Listesi:\n{stock_list}"

# Gradio arayüzü
with gr.Blocks() as demo:
    gr.Markdown("# Stok Takip Programı")

    # Ürün ekleme arayüzü
    with gr.Row():
        gr.Markdown("### Ürün Ekle")
        product_name_input = gr.Textbox(label="Ürün Adı")
        quantity_input = gr.Number(label="Miktar")
        add_button = gr.Button("Ürün Ekle")
        add_output = gr.Textbox(label="Durum")
        
    add_button.click(add_product, inputs=[product_name_input, quantity_input], outputs=add_output)

    # Stok güncelleme arayüzü
    with gr.Row():
        gr.Markdown("### Stok Güncelle")
        product_name_update = gr.Textbox(label="Ürün Adı")
        quantity_change = gr.Number(label="Değişim Miktarı (+/-)")
        update_button = gr.Button("Stok Güncelle")
        update_output = gr.Textbox(label="Durum")
        
    update_button.click(update_stock, inputs=[product_name_update, quantity_change], outputs=update_output)

    # Stok görüntüleme arayüzü
    with gr.Row():
        gr.Markdown("### Stok Görüntüle")
        view_button = gr.Button("Stok Listele")
        view_output = gr.Textbox(label="Stok Durumu")
        
    view_button.click(view_inventory, outputs=view_output)

# Uygulamayı başlat
demo.launch()
