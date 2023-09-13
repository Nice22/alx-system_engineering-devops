#!/bin/bash
#informations à partir du fichier JSON
DOMAIN="holb2023fs3eft.tech"
IP_ADDRESS="54.237.53.245"
WHOIS_SERVER="whois.nic.tech"

# Récupérer l'enregistrement WHOIS à partir du serveur WHOIS
WHOIS_RESPONSE=$(whois -h $WHOIS_SERVER $DOMAIN)

# Vérifier si le domaine est disponible
if echo "$WHOIS_RESPONSE" | grep -q "DOMAIN NOT FOUND"; then
    echo "Le domaine $DOMAIN est disponible."
    
    # TODO: Appeler l'API de votre fournisseur DNS pour mettre à jour les enregistrements
    # Exemple: Utiliser l'API de Cloudflare, GoDaddy, etc.
    # Assurez-vous d'avoir les informations d'authentification et l'URL de l'API appropriées.
    
else
    echo "Le domaine $DOMAIN n'est pas disponible."
fi

