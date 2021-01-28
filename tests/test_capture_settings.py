import pytest


@pytest.mark.skip("skip until migrated to snappi")
def test_capture_settings(serializer, api, tx_port, options):
    """Demonstrates how to configure basic capture settings
    """
    config = Config(ports=[tx_port], options=options)

    src = MacAddressFilter(mac='source',
                           filter='0000faceface',
                           mask='000000000000')
    dst = MacAddressFilter(mac='destination',
                           filter='0000faceface',
                           mask='000000000000')
    custom = CustomFilter(filter='fffefdfcfbfa',
                          mask='000000000000',
                          offset=50)

    config.captures.append(
        Capture(name='capture',
                port_names=[tx_port.name],
                choice=[
                    BasicFilter(src, and_operator=False, not_operator=True),
                    BasicFilter(dst, and_operator=False, not_operator=True),
                    BasicFilter(custom, and_operator=False, not_operator=True)
                ]))

    api.set_state(State(ConfigState(config=config, state='set')))


if __name__ == '__main__':
    pytest.main(['-s', __file__])