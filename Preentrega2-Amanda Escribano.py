#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install openai


# In[ ]:


import openai


# In[ ]:


# Configurar la API key (debes agregar tu clave)
api_key = "TU_API_KEY"

def generate_content(prompt, model="gpt-4", temperature=0.7):
    """Genera texto basado en el prompt utilizando la API de OpenAI."""
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )
    return response["choices"][0]["message"]["content"]


# In[ ]:


# Ejemplo de prompts iniciales vs. optimizados
initial_prompt = "Escribe una descripción de LinkedIn para un especialista en IA."
optimized_prompt = (
    "Eres un experto en branding personal. Redacta una descripción de LinkedIn atractiva, en tono profesional, "
    "que resalte logros clave, experiencia en IA y gestión de riesgos, con un llamado a la acción al final."
)


# In[ ]:


# Generar textos
initial_text = generate_content(initial_prompt)
optimized_text = generate_content(optimized_prompt)


# In[ ]:


# Mostrar resultados
print("--- Prompt Inicial ---")
print(initial_text)
print("\n--- Prompt Optimizado ---")
print(optimized_text)

