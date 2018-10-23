from oscar.apps.partner.strategy import UseFirstStockRecord, StockRequired, FixedRateTax, Structured, TaxInclusiveFixedPrice


class Selector(object):
    def strategy(self, request=None, user=None, **kwargs):
        return Default(request)


class Default(UseFirstStockRecord, StockRequired, FixedRateTax, Structured):
    def pricing_policy(self, product, stockrecord):
        sale_price = getattr(stockrecord, 'saleprice', None)
        if sale_price:
            rate = self.get_rate(product, stockrecord)
            exponent = self.get_exponent(stockrecord)
            tax = (stockrecord.saleprice.price_excl_tax * rate).quantize(exponent)
            return TaxInclusiveFixedPrice(
                currency=stockrecord.price_currency,
                excl_tax=stockrecord.saleprice.price_excl_tax,
                tax=tax)
        return super().pricing_policy(product, stockrecord)
