<?php

namespace DevopsProject;

use PHPUnit\Framework\TestCase;

class DevopsClassTest extends TestCase
{

    public function testSayHello()
    {
        $hello = new DevopsClass();
        $this->assertEquals("Hello World", $hello->sayHello());
    }
}
