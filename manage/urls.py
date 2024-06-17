from django.urls import path

from manage.views import user, role, power, log

urlpatterns = [
    # 用户管理
    path("user-manage", user.user_manage),  # 用户管理页面
    path("user-query", user.user_query),  # 用户查询
    path("user-add", user.user_add),  # 用户新增
    path("user-role-query", user.user_role_query),  # 用户新增页面查询所有角色
    path("user-delete", user.user_delete),  # 用户删除
    path("user-multi-delete", user.user_multi_delete),  # 用户批量删除
    path("user-cell-edit", user.user_cell_edit),  # 用户表格单元编辑
    path("user-role-edit", user.user_role_edit),  # 用户角色编辑
    path("user-enable", user.user_enable),  # 用户启用禁用
    # 角色管理
    path("role-manage", role.role_manage),  # 角色管理
    path("role-query", role.role_query),  # 角色查询
    path("role-add", role.role_add),  # 角色新增
    path("role-delete", role.role_delete),  # 角色删除
    path("role-cell-edit", role.role_cell_edit),  # 角色表格单元边界
    path("role-enable", role.role_enable),  # 角色使能
    path("role-power", role.role_power),  # 角色权限分配
    path("role-power-save", role.role_power_save),  # 角色权限保存
    # 系统管理
    path("power-manage", power.power_manage),  # 系统管理页面
    path("power-query", power.power_query),  # 权限查询
    path("power-add", power.power_add),  # 权限新增
    path("power-sub-query", power.power_sub_query),  # 权限子项查询
    path("power-delete", power.power_delete),  # 权限删除
    path("power-multi-delete", power.power_multi_delete),  # 权限批量删除
    path("power-cell-edit", power.power_cell_edit),  # 权限表格单元边界
    path("power-enable", power.power_enable),  # 权限使能
    # 日志管理
    path("log-manage", log.log_manage),  # 日志管理
    path("log-query", log.log_query),  # 日志查询
    path("log-delete", log.log_delete),  # 日志删除
]
