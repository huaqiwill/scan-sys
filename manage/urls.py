


from django.urls import path

from manage.views import user_manage, role_manage, power_manage, log_manage

urlpatterns = [
    # 用户管理
    path("user-manage", user_manage.user_manage),  # 用户管理页面
    path("user-query", user_manage.user_query),  # 用户查询
    path("user-add", user_manage.user_add),  # 用户新增
    path("user-role-query", user_manage.user_role_query),  # 用户新增页面查询所有角色
    path("school-query", user_manage.school_query),  # 用户新增页面查询所有学校
    path("user-delete", user_manage.user_delete),  # 用户删除
    path("user-multi-delete", user_manage.user_multi_delete),  # 用户批量删除
    path("user-cell-edit", user_manage.user_cell_edit),  # 用户表格单元编辑
    path("user-role-edit", user_manage.user_role_edit),  # 用户角色编辑
    path("user-enable", user_manage.user_enable),  # 用户启用禁用
    # 角色管理
    path("role-manage", role_manage.role_manage),  # 角色管理
    path("role-query", role_manage.role_query),  # 角色查询
    path("role-add", role_manage.role_add),  # 角色新增
    path("role-delete", role_manage.role_delete),  # 角色删除
    path("role-cell-edit", role_manage.role_cell_edit),  # 角色表格单元边界
    path("role-enable", role_manage.role_enable),  # 角色使能
    path("role-power", role_manage.role_power),  # 角色权限分配
    path("role-power-save", role_manage.role_power_save),  # 角色权限保存
    # 系统管理
    path("power-manage", power_manage.power_manage),  # 系统管理页面
    path("power-query", power_manage.power_query),  # 权限查询
    path("power-add", power_manage.power_add),  # 权限新增
    path("power-sub-query", power_manage.power_sub_query),  # 权限子项查询
    path("power-delete", power_manage.power_delete),  # 权限删除
    path("power-multi-delete", power_manage.power_multi_delete),  # 权限批量删除
    path("power-cell-edit", power_manage.power_cell_edit),  # 权限表格单元边界
    path("power-enable", power_manage.power_enable),  # 权限使能
    # 日志管理
    path("log-manage", log_manage.log_manage),  # 日志管理
    path("log-query", log_manage.log_query),  # 日志查询
    path("log-delete", log_manage.log_delete),  # 日志删除
]
