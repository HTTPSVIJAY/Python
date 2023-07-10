class geeks:
	course = 'DSA'

	def purchase(obj):
		print("Purchase course : ", obj.course)


geeks.purchase = classmethod(geeks.purchase)
geeks.purchase()
