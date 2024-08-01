from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow, BaseEditWindow, make_combo_box, ComboBoxWithStore
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, Group, User
from m3_ext.ui import all_components as ext

class ContentTypePack(ObjectPack):
    model = ContentType
    add_to_desktop = True
    add_window = edit_window = ModelEditWindow.fabricate(ContentType)

class PermissionEditWindow(BaseEditWindow):

    def _init_components(self):
        super(PermissionEditWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label='Name',
            name='name',
            allow_blank=False,
            anchor='100%')

        self.field__content_type = ext.ExtDictSelectField(
            label='Content Type',
            name='content_type_id',
            allow_blank=False,
            pack=ContentTypePack,
        )

        self.field__codename = ext.ExtStringField(
            label='Codename',
            name='codename',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        super(PermissionEditWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_type,
            self.field__codename,
        ))

    def set_params(self, params):
        super(PermissionEditWindow, self).set_params(params)
        self.height = 'auto'

class PermissionPack(ObjectPack):
    model = Permission
    add_to_desktop = True
    add_window = edit_window = PermissionEditWindow

class GroupPack(ObjectPack):
    model = Group
    add_to_desktop = True
    add_window = edit_window = ModelEditWindow.fabricate(Group)

class UserEditWindow(BaseEditWindow):

    def _init_components(self):
        super(UserEditWindow, self)._init_components()

        self.field__username = ext.ExtStringField(
            label='Username',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__password = ext.ExtStringField(
            label='Password',
            name='password',
            allow_blank=False,
            anchor='100%',
            input_type='password')

        self.field__first_name = ext.ExtStringField(
            label='First Name',
            name='first_name',
            allow_blank=True,
            anchor='100%')

        self.field__last_name = ext.ExtStringField(
            label='Last Name',
            name='last_name',
            allow_blank=True,
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label='Email',
            name='email',
            allow_blank=True,
            anchor='100%',
            vtype='email')

        self.field__is_staff = ext.ExtCheckBox(
            label='Staff status',
            name='is_staff')

        self.field__is_active = ext.ExtCheckBox(
            label='Active',
            name='is_active')

        self.field__is_superuser = ext.ExtCheckBox(
            label='Superuser status',
            name='is_superuser')

        self.field__date_joined = ext.ExtDateField(
            label='Date joined',
            name='date_joined',
            allow_blank=False,
            anchor='100%',
            format='d.m.Y')  

    def _do_layout(self):
        super(UserEditWindow, self)._do_layout()
        self.form.items.extend((
            self.field__username,
            self.field__password,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__is_staff,
            self.field__is_active,
            self.field__is_superuser,
            self.field__date_joined,
        ))

    def set_params(self, params):
        super(UserEditWindow, self).set_params(params)
        self.height = 'auto'

class UserPack(ObjectPack):
    model = User
    add_to_desktop = True
    add_window = edit_window = UserEditWindow
