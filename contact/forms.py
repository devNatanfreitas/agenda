from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept':'image/*',
            }
        )
    )

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'category','picture',)

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if not first_name:
            raise ValidationError("Nome não pode estar vazio.", code='invalid')

        if any(char.isdigit() for char in first_name):
            raise ValidationError("Nome não pode conter números.", code='invalid')

        if not first_name.isalpha():
            raise ValidationError("Nome deve conter apenas caracteres alfabéticos.", code='invalid')

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        if not last_name:
            raise ValidationError("Sobrenome não pode estar vazio.", code='invalid')

        if any(char.isdigit() for char in last_name):
            raise ValidationError("Sobrenome não pode conter números.", code='invalid')

        if not last_name.isalpha():
            raise ValidationError("Sobrenome deve conter apenas caracteres alfabéticos.", code='invalid')

        return last_name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not phone:
            raise ValidationError("Número de telefone não pode estar vazio.", code='invalid')

        if not phone.isdigit():
            raise ValidationError("Número de telefone deve conter apenas dígitos.", code='invalid')

        if not (10 <= len(phone) <= 15):
            raise ValidationError("Número de telefone deve ter entre 10 e 15 dígitos.", code='invalid')

        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            raise ValidationError("E-mail não pode estar vazio.", code='invalid')

        if '@' not in email or '.' not in email.split('@')[-1]:
            raise ValidationError("Insira um endereço de e-mail válido.", code='invalid')

        return email

    def clean_description(self):
        description = self.cleaned_data.get('description')

        if not description:
            raise ValidationError("Descrição não pode estar vazia.", code='invalid')

        if len(description) < 10:
            raise ValidationError("Description must be at least 10 characters long.", code='invalid')

        return description

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'username', 'password1', 'password2',)

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if not first_name:
            raise ValidationError("First name cannot be empty.", code='invalid')

        if any(char.isdigit() for char in first_name):
            raise ValidationError("First name cannot contain numbers.", code='invalid')

        if not first_name.isalpha():
            raise ValidationError("First name must contain only alphabetic characters.", code='invalid')

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        if not last_name:
            raise ValidationError("Last name cannot be empty.", code='invalid')

        if any(char.isdigit() for char in last_name):
            raise ValidationError("Last name cannot contain numbers.", code='invalid')

        if not last_name.isalpha():
            raise ValidationError("Last name must contain only alphabetic characters.", code='invalid')

        return last_name

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if not username:
            raise ValidationError("Username cannot be empty.", code='invalid')

        if len(username) < 5:
            raise ValidationError("Username must be at least 5 characters long.", code='invalid')

        if User.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken.", code='invalid')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            raise ValidationError("Email cannot be empty.", code='invalid')

        if '@' not in email or '.' not in email.split('@')[-1]:
            raise ValidationError("Enter a valid email address.", code='invalid')

        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.", code='invalid')

        return email

class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )
    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )
 
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user
    
    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não batem')
                )
        return super().clean()
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email
        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este e-mail', code='invalid')
                )
        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )
        return password1
