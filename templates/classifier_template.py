# Fitness: {{ chromosome.fitness }}
def classify(hand):
	hand_confidences = [0 for i in range(10)]
	
	{#- Generate if conditions -#}
	{% for gene in chromosome.genes %}
	
	# Mutation Resistance: {{ 100.0 * gene.mutation_resistance }}%
	if {% for condition in gene.conditions -%}
			({{- condition.__str__() }})
			{%- if condition != gene.conditions[-1] %} and {% else %}:{% endif %}
		{%- endfor %}
	
		{#- Generate if gene is true action #}
		hand_confidences[{{ gene.hand_class }}] += {{ gene.confidence }}
		
	{%- endfor %}
	
	{# Generate classification decision -#}
	if max(hand_confidences) >= 100:
		hand.assigned_class = hand_confidences.index(max(hand_confidences))
	else:
		hand.assigned_class = 1