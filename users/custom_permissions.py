from rest_framework import permissions
from rest_framework.exceptions import APIException
from rest_framework import status

class SuperAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user is None:
            return False
        roles = request.user.roles.all()
        for rol in roles:
            if "super_admin" == rol.name:
                return True
        return False

class UserAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user is None:
            return False
        roles = request.user.roles.all()
        for rol in roles:
            if "admin" == rol.name:
                return True
        return False
    
class ManagerUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user is None:
            return False
        roles = request.user.roles.all()
        for rol in roles:
            if "manager" == rol.name:
                return True
        return False
        
class BecadoUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user is None:
            return False
        roles = request.user.roles.all()
        for rol in roles:
            if "becado" == rol.name:
                return True
        return False
