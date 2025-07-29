from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from datetime import datetime
import os

def generar_pdf_productos(productos, archivo="productos_completos.pdf", logo_path=None):
    """
    Genera un PDF con la lista completa de productos.

    Args:
        productos: Lista de objetos Producto
        archivo: Nombre del archivo PDF a generar
        logo_path: Ruta al archivo de logo (opcional)

    Returns:
        str: Mensaje de éxito o error.
    """
    try:
        if not productos:
            raise ValueError("La lista de productos está vacía. No se puede generar el PDF.")

        # Configurar documento con márgenes personalizados
        doc = SimpleDocTemplate(
            archivo,
            pagesize=landscape(letter),
            rightMargin=20,
            leftMargin=20,
            topMargin=30,
            bottomMargin=30
        )

        elementos = []

        # Crear estilos personalizados
        estilos = getSampleStyleSheet()
        estilo_titulo = ParagraphStyle(
            'TituloPrincipal',
            parent=estilos['Heading1'],
            fontSize=24,
            alignment=1,
            spaceAfter=12,
            textColor=colors.HexColor('#2C3E50')
        )
        estilo_fecha = ParagraphStyle(
            'Fecha',
            parent=estilos['Normal'],
            fontSize=10,
            alignment=1,
            spaceBefore=6,
            textColor=colors.gray
        )

        # Crear estilo para nombres de productos con ajuste de texto
        estilo_nombre = ParagraphStyle(
            'NombreProducto',
            parent=estilos['Normal'],
            fontSize=10,
            leading=12,  # Espacio entre líneas
        )

        # Añadir logo si se proporciona
        if logo_path and os.path.exists(logo_path):
            logo = Image(logo_path)
            logo.drawHeight = 1.2 * inch
            logo.drawWidth = 1.2 * inch
            elementos.append(logo)
            elementos.append(Spacer(1, 0.3 * inch))

        # Añadir título y fecha
        elementos.append(Paragraph("Catálogo de Productos", estilo_titulo))
        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
        elementos.append(Paragraph(f"Generado el: {fecha_actual}", estilo_fecha))
        elementos.append(Spacer(1, 0.5 * inch))

        # Preparar datos para la tabla
        datos_tabla = [["ID", "Nombre", "Precio", "Categoría", "Stock", "Calificación"]]
        for p in productos:
            # Convertir nombre de producto a Paragraph para permitir ajuste de texto
            nombre_formateado = Paragraph(p.nombre, estilo_nombre)
            datos_tabla.append([
                str(p.id),
                nombre_formateado,  # Usar nombre formateado
                f"${p.precio:.2f}",
                p.categoria,
                str(p.stock),
                f"{p.calificacion_promedio:.1f} ★"
            ])

        # Crear la tabla con mayor ancho para la columna Nombre
        tabla = Table(datos_tabla, colWidths=[50, 200, 80, 100, 60, 80])

        # Estilo de la tabla
        estilo_tabla = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498DB')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#EBF5FB')),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Alineación vertical centrada
        ])

        # Alternar colores de filas
        for i in range(1, len(datos_tabla)):
            if i % 2 == 0:
                estilo_tabla.add('BACKGROUND', (0, i), (-1, i), colors.HexColor('#D6EAF8'))

        tabla.setStyle(estilo_tabla)
        elementos.append(tabla)

        # Clase para pie de página
        class PieDePagina:
            def __call__(self, canvas, doc):
                canvas.saveState()
                canvas.setFont('Helvetica', 9)
                canvas.drawString(30, 15, f"Página {doc.page}")
                canvas.restoreState()

        # Construir el PDF
        doc.build(elementos, onFirstPage=PieDePagina(), onLaterPages=PieDePagina())

        return f"PDF generado exitosamente: {archivo}"

    except Exception as e:
        return f"Error: {e}"
