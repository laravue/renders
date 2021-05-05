// environmentSetBaseplateColor(int color)
with obj_server {
    BasePlateColor = argument0;
}
with obj_client {
    buffer_clear(global.BUFFER);
    buffer_write_uint8(global.BUFFER, 7);
    buffer_write_string(global.BUFFER, "BaseCol");
    buffer_write_uint32(global.BUFFER, argument0);
    socket_write_message(SOCKET, global.BUFFER);
}
