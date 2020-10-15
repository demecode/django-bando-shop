from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields
from django.forms.utils import pretty_name


# Each product will have a name, price, optional description, optional image and availability

class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=250,
                              db_index=True),
        slug=models.SlugField(max_length=250,
                              db_index=True,
                              unique=True)
    )

    class Meta:
        # ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=250, db_index=True),
        slug=models.SlugField(max_length=250, db_index=True),
        description=models.TextField(blank=True)
    )

    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ('name',)
    #     index_together = (('id',
    #                        'slug'),)
    # index together to specify an index for id and slug field together. Will be using for quering

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])
