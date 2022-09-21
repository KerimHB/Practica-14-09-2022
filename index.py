from flask import Flask, render_template, request, session, redirect, url_for, g

class Usuario:
    def __init__(self, id, username, password):
        self.id=id
        self.username=username
        self.password=password
    
    def __repr__(self) -> str:
        return f'<Usuario:{self.username}>'  #__repr__ ampliar

usuarios=[]
usuarios.append(Usuario(id=1, username='Kerim', password='123456'))
usuarios.append(Usuario(id=2, username='Reaper', password='654321'))
usuarios.append(Usuario(id=3, username='Mamamlon', password='123123'))


app=Flask(__name__)
app.secret_key='123456'

@app.before_request
def before_request():
    g.usuario = None
    if 'usuario_id' in session:
        usuario= [x for x in usuarios if x.id == session['usuario_id']][0]
        g.usuario=usuario


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        session.pop('usuario_id', None)  #definir pop
        username=request.form['username']
        password=request.form['password']

        usuario=[x for x in usuarios if x.username == username][0]
        if usuario and usuario.password == password:
            session['usuario_id']=usuario.id
            return redirect(url_for('perfil'))
        return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/perfil')
def perfil():
    if g.usuario==None:
        return redirect(url_for('login'))
    return render_template('perfil.html')

if __name__=='__main__':
    app.run(debug=True)