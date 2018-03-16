from .. app import db
import datetime

# On crée notre modèle
class Comment(db.Model):
	comment_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
	comment_nom = db.Column(db.Text)
	comment_commentaire = db.Column(db.Text, nullable=False)
	comment_lien = db.Column(db.Text, nullable=False)
	#comment_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	comment_user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
	user = db.relationship("User", back_populates="comment")

	@staticmethod
	def creercomment(nom, commentaire, lien):
		erreurs = []
		if not nom:
		    erreurs.append("Le nom fourni est vide")
		if not commentaire:
			erreurs.append("Le commentaire fourni est vide")
		if not lien:
			erreurs.append("Le lien fourni est vide")
		
		# On vérifie que le lien n'existe pas 
		#uniques = Place.query.filter(
		#    db.or_(Place.place_nom == nom)
		#).count()
		#if uniques > 0:
		    #erreurs.append("Le nom de lieu existe déjà dans notre base de données")

		# Si on a au moins une erreur
		if len(erreurs) > 0:
		    return False, erreurs

		# On crée un lieu
		comment = Comment(
		    comment_nom=nom,
		    comment_commentaire=commentaire,
		    comment_lien=lien
		)

		try:
            		# On l'ajoute au transport vers la base de données
            		db.session.add(comment)
            		# On envoie le paquet
            		db.session.commit()

            	# On renvoie le commentaire
            		return True, comment
		except Exception as erreur:
            		return False, [str(erreur)]