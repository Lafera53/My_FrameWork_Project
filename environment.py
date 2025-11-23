def before_all(context):
	context.config.setup_logging()

	def before_feature(context, feature):
		pass

	def before_scenario(context, scenario):
		pass

	def before_step(context, step):
		pass

	def after_step(context, step):
		pass

	def after_scenario(context, scenario):
		pass

	def after_feature(context, feature):
		pass

	def after_all(context):
		pass
