# Use uma imagem base do Nginx específica
FROM nginx:stable-bookworm-perl

# Copie a configuração personalizada do Nginx para o container
COPY config/nginx.conf /etc/nginx/nginx.conf

RUN apt update && apt upgrade -y \
    && apt install tree -y

# Copie arquivos de site estático ou outros recursos, se necessário
# COPY html /usr/share/nginx/html

# Expõe a porta padrão do Nginx
EXPOSE 80
EXPOSE 443

# Comando padrão para iniciar o Nginx
CMD ["nginx", "-g", "daemon off;"]
