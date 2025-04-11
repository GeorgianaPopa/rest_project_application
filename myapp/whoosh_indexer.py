from whoosh.fields import Schema, TEXT, ID
from whoosh.index import create_in
from whoosh.analysis import StemmingAnalyzer
import os
from .models import Product

def create_search_index():
    index_dir = "whoosh_index"
    if os.path.exists(index_dir):
        import shutil
        shutil.rmtree(index_dir)

    os.mkdir(index_dir)

    schema = Schema(
        id=ID(stored=True, unique=True),
        name=TEXT(stored=True, analyzer=StemmingAnalyzer()),
        description=TEXT(stored=True, analyzer=StemmingAnalyzer())
    )

    ix = create_in(index_dir, schema)
    writer = ix.writer()

    for product in Product.objects.all():
        writer.add_document(
            id=str(product.id),
            name=product.name,
            description=product.description
        )

    writer.commit()
